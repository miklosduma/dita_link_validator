# dita-link-validator
Python command-line utility for checking external links stored in a ditamap as keys 

## Dependencies
* Unix/Linux
* Python 2.7
* Python libraries:
  * requests - `pip install requests`
  * termcolor - `pip install termcolor`

## Expected ditamap structure
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
<p>Visit the <xref keyref="link_sparkl home"/> for more information on SPARKL.</p>
```

## Using the checker tool
Invoke the `link_checker.py` script from the command-line as `python [PATH_TO_SCRIPT] [PATH_TO_DITAMAP].  

For example, the sample code below runs the script on the included test ditamap.
```
$ cd dita-link-validator
$ python link_checker/link_checker.py test/test_files/test_links.ditamap

Checking links in file: test/test_files/test_links.ditamap
Link checked: http://sparkl.com
Link checked: https://en.wikipedia.org/wiki/Darwin_Information_Typing_Architecture
ERROR!!!!! Failed to connect to link: http://no-such-link
ERROR!!!!! Link is not well-formed. Check link in your browser: missing_http_schema
Links to be checked: http://no-such-link, missing_http_schema
```
 
