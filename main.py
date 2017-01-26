#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import caesar

def buildPage(content):
    header = "<h2>Web Caesar</h2>"
    rotation = "<label>Rotation amount<br><input type='number' name='rotation'/></label>"
    textbox = "<label>Type a message<br><textarea name='message'>"+ content + "</textarea></label>"
    submit = "<input type='submit'/>"
    content = header + "<form method='post'>" + rotation + "<br>" + textbox + "<br>" + submit + "</form>"
    return content

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = buildPage("")
        self.response.write(page)

    def post(self):
        message = self.request.get('message')
        rotate = int(self.request.get('rotation'))
        secret = caesar.encrypted(message, rotate)
        page = buildPage(secret)
        self.response.write(page)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
