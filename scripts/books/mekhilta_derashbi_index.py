# -*- coding: utf-8 -*-

import sys
import urllib
import urllib2
from urllib2 import URLError, HTTPError
import json
import base64

sys.path.append("C:\\Users\\Izzy\\git\\Sefaria-Project")
from sefaria.model import *

# server = 'dev.sefaria.org'
server = "localhost:8000"

def post_texts_api(text_obj, ref, method="Post"):
    url = 'http://' + server + '/api/v2/raw/index/{}'.format(ref)
    json_text = json.dumps(text_obj)
    values = {
        'json': json_text,
        'apikey': apikey
    }
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    req.get_method = lambda: method
    try:
        response = urllib2.urlopen(req)
        print response.read()
    except HTTPError, e:
        print 'Error code: ', e.code
        print e.read()

root = SchemaNode()
root.add_title("Mekhilta DeRabbi Shimon Bar Yochai", "en", primary=True)
root.add_title("Mekhilta DeRabbi Shimon", "en", primary=False)
root.add_title("Mekhilta DeRashbi", "en", primary=False)
root.add_title(u"מכילתא דרבי שמעון בר יוחאי", "he", primary=True)
root.add_title(u"מכילתא דרבי שמעון ", "he", primary=False)
root.add_title(u"מכילתא דרשב\"י", "he", primary=False)
root.key = "Mekhilta DeRabbi Shimon Bar Yochai"

# Main Body of the text
main_body = JaggedArrayNode()
main_body.depth = 2
main_body.sectionNames = ["Chapter", "Verse"]
main_body.addressTypes = ["Integer", "Integer"]
main_body.default=True
main_body.key = "default"

# Additions
additions = JaggedArrayNode()
additions.add_title(u"הוספה", "he", primary=True)
additions.add_title("Additions", "en", primary=True)
additions.depth = 2
additions.sectionNames = ["Chapter", "Verse"]
additions.addressTypes = ["Integer", "Integer"]
additions.key = "Additions"

root.append(main_body)
root.append(additions)

root.validate()

indx = {
    "title": "Mekhilta DeRabbi Shimon Bar Yochai",
    "categories": ["Midrash", "Halachic Midrash"],
    "schema": root.serialize()
}



#Index(indx).save()
# post_texts_api(indx, "Mekhilta%20DeRabbi%20Shimon%20Bar%20Yochai", "DELETE")


post_texts_api(indx, "Mekhilta%20DeRabbi%20Shimon%20Bar%20Yochai")

# Footnote Index
footnote_index = {
    "title": "Footnotes",
    "titleVariants": ["Footnotes"],
    "heTitle": "הערות שוליים",
    "heTitleVariants": ["הערות שוליים"],
    "categories": ["Commentary"]
}

# post_texts_api(footnote_index, "Footnotes%20on%20Mekhilta%DeRabbi%Shimon%Bar%Yochai", "DELETE")
post_texts_api(footnote_index, "Footnotes")
