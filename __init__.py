# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from mycroft import MycroftSkill, intent_file_handler


# TODO - Localization

class SpeakSkill(MycroftSkill):
    @intent_file_handler("speak.intent")
    def speak_back(self, message):
        """
            Repeat the utterance back to the user.

        """
        repeat = message.data.get("sentence", "")
        self.speak(repeat.strip())


def create_skill():
    return SpeakSkill()
