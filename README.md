# dita-link-validator
_Python command-line utility for finding broken links in a DITA project._

## Dependencies
* DITA-OT or a software that relies on it
  > For example, Oxygen XML.
* Unix/Linux
* Python 2.7
* Python libraries:
  * requests - `pip install requests`
  * termcolor - `pip install termcolor` 

## Expected structure
The application assumes:
* External links are added to your ditamap as first-level `topicref` elements
* All of these `topicref` elements have the `keys` attribute
  > You may keep all external links in a separate ditamap and reuse the whole map wherever needed. 

```xml
<!-- Expected ditamap structure -->
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

<!-- Sample topic using the link -->
<topic>
 <title>Referencing links in topics</title>
   <p>Visit the <xref keyref="link_sparkl_home"/> for more information on SPARKL.</p>
</topic>
```
The script does not work on links embedded directly into your content. Storing links in a ditamap and referencing them through keys also makes it easier to manage and reuse those links.

## Using the tool
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
The script:
1. Takes all first level `topicref` children of the specified ditamap
2. Keeps only the ones that have the `format="html"` attribute
3. Retrieves the links from the `href` attributes and pings them
4. Collects and lists all broken links

## Running tests
```
$ cd dita_link_validator
$ python setup.py test
```
> The tests use the `nose` library. If not already installed, `setup.py` tries to install it.
