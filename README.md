# dita-link-validator
Python command-line utility for checking external links stored in a ditamap as keys. 

Referencing websites through keys makes it easier to manage and reuse those links. 
> The script will not work on links embedded directly into your content. 

## Dependencies
* Unix/Linux
* Python 2.7
* Python libraries:
  * requests - `pip install requests`
  * termcolor - `pip install termcolor`

## Expected ditamap structure
All external links should be added to the ditamap as keys. The script:
1. Takes all first level `topicref` children from a ditamap
2. Keeps only the ones that have `scope="external"` on them
3. Retrieves the links from `hrefs` and pings them
> It is best to have a separate ditamap for storing links.  
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
## Referencing links in place of use
```xml
<p>Visit the <xref keyref="link_sparkl_home"/> for more information on SPARKL.</p>
```

## Using the checker tool
Invoke the `link_checker.py` script from the command-line as `python [PATH_TO_SCRIPT] [PATH_TO_DITAMAP]`.  

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
 
