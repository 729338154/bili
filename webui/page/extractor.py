# (C) 2019-2020 lifegpc
# This file is part of bili.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from . import InvalidInputEroor, new_Session
from regex import search, I
from requests import Session


class extractor:
    _VALID_URI = r''
    _groupdict = {}
    _inp = ""
    _r: Session = None

    def __init__(self, inp: str):
        "对uri进行处理"
        re = search(self._VALID_URI, inp, I)
        if re == None:
            raise InvalidInputEroor()
        self._inp = inp
        self._groupdict = re.groupdict()
        self._r = new_Session()

    def _handle(self):
        "具体处理"
        return {'code': 0, 'type': 'unknown'}

    def _addcookies(self, vq: int = 125):
        "增加具体的cookies,vq为视频画质"
        self._r.cookies.set('CURRENT_QUALITY', str(
            vq), domain='.bilibili.com', path='/')
        self._r.cookies.set('CURRENT_FNVAL', '80',
                            domain='.bilibili.com', path='/')
        self._r.cookies.set('laboratory', '1-1',
                            domain='.bilibili.com', path='/')
        self._r.cookies.set('stardustvideo', '1',
                            domain='.bilibili.com', path='/')
