# dita-link-validator
Python command-line utility for checking external links stored in a ditamap as keys. 

Referencing websites through keys makes it easier to manage and reuse those links. 
> The script does not work on links embedded directly into your content. 

## Dependencies
* Unix/Linux
* Python 2.7
* Python libraries:
  * requests - `pip install requests`
  * termcolor - `pip install termcolor`

## Expected ditamap structure
_Add all external links to the ditamap as keys._

The script:
1. Takes all first level `topicref` children of a ditamap
2. Keeps only the ones that have the `format="html"` attribute
3. Retrieves the links from the `href` attributes and pings them
> It is best to keep all external links in a separate ditamap.  
```xml
<map>
  <title>Test Links Map</title>
  <topicref keys="link_sparkl_home" format="html" scope="external"
    href="http://sparkl.com" navtitle="SPARKL home page">
    <topicmeta>
      <keywords>
        <keyword>SPARKL home page</keyword>
      </keywords>
    </topicmeta>
  </topicref>
  <!-- More links included as keys -->
</map>
```
## Referencing links in topics
```xml
<p>Visit the <xref keyref="link_sparkl_home"/> for more information on SPARKL.</p>
```

## Using the checker tool
Invoke the `link_checker.py` script from the command-line as `python link_checker.py [PATH_TO_DITAMAP]`.  

For example, the sample code below runs the script on the included test ditamap.
```
$ cd dita_link_validator/dita_link_validator
$ python link_checker.py tests/test_files/test_links.ditamap

Checking links in file: tests/test_files/test_links.ditamap
Link checked: http://sparkl.com
Link checked: https://en.wikipedia.org/wiki/Darwin_Information_Typing_Architecture
ERROR!!!!! Failed to connect to link: http://no-such-link
ERROR!!!!! Link is not well-formed. Check link in your browser: missing_http_schema
Links to be checked: http://no-such-link, missing_http_schema
```
 
