# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin


class QRprintPlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.AssetPlugin):
    def on_after_startup(self):
        self._logger.info("QRprint enabled (more: %s)" % self._settings.get(["url"]))

    def get_settings_defaults(self):
        return dict(url="https://en.wikipedia.org/wiki/Hello_world")

    def get_template_vars(self):
        return dict(url=self._settings.get(["url"]))

__plugin_name__ = "QRprint"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = QRprintPlugin()
