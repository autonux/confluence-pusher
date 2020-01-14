SOURCE_FOLDER = "./engineering-standards"
CONFLUENCE_SPACE = '~613673678'
CONFLUENCE_URL = 'https://vibrato.atlassian.net'
CONFLUENCE_USERID = 'konstantin.vanyushov@servian.com'
CONFLUENCE_OATOKEN = 'ozL4ruBp6vyjIKpj14la749B'
CONFLUENCE_SECTION_CONTENT_FILE = "README.md"
CONFLUENCE_TABLE_OF_CONTENTS = "SUMMARY.md"
CONFLUENCE_FILTER_NAME = 'confluence.lua'

CONFLUENCE_ROOT_PAGE_NAME = SOURCE_FOLDER.replace('./', '')

CONFLUENCE_FILTER_URL = \
    "https://raw.githubusercontent.com/jpbarrette/pandoc-confluence-writer/master/" + \
    CONFLUENCE_FILTER_NAME
UPDATE_CONFLUENCE_FILTER = "wget " + \
    CONFLUENCE_FILTER_URL + " -O " + CONFLUENCE_FILTER_NAME

CONFLUENCE_FILE_EXTENSION = '.cf'
TMP_FILE = "_filetemp.tmp"

MD_EXTENSION = '.md'
MD_HEADER_START = '# '

IMG_TAG_START = '<ac:image><ri:attachment ri:filename="'
IMG_TAG_END = '" /></ac:image>'

GITBOOK_TAB_BEGIN = '{% tab'
GITBOOK_TAB_END = '%}'
GITBOOK_TABS_END = 'tabs %}'

SVG_EXTENSION = ".svg"
SVG_W_START = 'width="'
SVG_W_END = 'px"'
SVG_H_START = 'height="'
SVG_H_END = 'px"'
SVG_VIEWBOX_TAG = 'viewBox="'

SVG_MAX_WIDTH = 1000
SVG_MAX_HEIGHT = 1500

CONFLUENCE_TAG_AC_STYLE_BEGIN = '<ac:structured-macro ac:macro-id="'
CONFLUENCE_TAG_AC_STYLE_END = '</style>]]></ac:plain-text-body></ac:structured-macro>'
CONFLUENCE_TAG_AC_DIV_BEGIN = '<ac:structured-macro ac:macro-id='
CONFLUENCE_TAG_AC_DIV_END = '</ac:structured-macro>'
CONFLUENCE_TAG_AC_IMAGE_BEGIN = '<ac:image>'
CONFLUENCE_TAG_AC_IMAGE_END = '</ac:image>'
CONFLUENCE_TAG_AC_IMAGE_BEGIN_WIDTH_1000 = \
    '<ac:image ac:align="center" ac:width="' + str(SVG_MAX_WIDTH) + '">'