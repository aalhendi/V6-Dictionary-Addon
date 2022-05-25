from aqt.qt import *
from .miutils import miAsk
from anki.utils import isWin, isMac
from anki.hooks import addHook
from aqt.utils import openLink


def checkForThirtyTwo():
	if isWin or isMac:
		if QT_VERSION_STR[0] != '6':
			msg = 'Please make sure you are on a 64-bit release of Anki with Qt6 support.'
			if miAsk(msg, customText = ["Take me there", "No"]):
				openLink("https://github.com/ankitects/anki/releases")


addHook("profileLoaded", checkForThirtyTwo)