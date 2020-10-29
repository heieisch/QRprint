# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import flask, json
from octoprint.server.util.flask import restricted_access
from octoprint.events import eventManager, Events

class QRprintPlugin(occtoprint.plugin.SettingsPlugin,
							octoprint.plugin.TemplatePlugin,
							octoprint.plugin.AssetPlugin,
							octoprint.plugin.StartupPlugin,
							octoprint.plugin.BlueprintPlugin,
							octoprint.plugin.EventHandlerPlugin):
	
	
    def on_after_startup(self):
        self._logger.info("QRprint enabled (test url: %s)" % self._settings.get(["url"]))

    def get_settings_defaults(self):
        return dict(qp_url="https://en.wikipedia.org/wiki/Hello_world",
		    qp_copydir="smb://fileserver/data",
		    qp_localdir="/qrprint/",
		    qp_sufix="/qrprint/"
									 )

    def get_template_vars(self):
        return dict(url=self._settings.get(["url"])
			
		    
    def start_next_print(self):
		sd = True
		    qr_input=
		    source= qp_copydir + qp_input + qp_sufix
		    dest=qp_localdir + qp_input + qp_sufix
				try:
		    			self._printer.copy_file(surce, dest)
		    			self._logger.info("copying file")
					self._printer.select_file(dest, sd)
					self._logger.info("selecting file")
					self._printer.start_print()
				except InvalidFileLocation:
					self._plugin_manager.send_plugin_message(self._identifier, dict(type="popup", msg="ERROR file not found"))
				except InvalidFileType:
					self._plugin_manager.send_plugin_message(self._identifier, dict(type="popup", msg="ERROR file not gcode"))
		
			

										
def get_template_configs(self):
		return [
			dict(type="settings", custom_bindings=False, template="qrprint_settings.jinja2"),
			dict(type="tab", custom_bindings=False, template="qrprint_tab.jinja2",
			dict(type="navbar", custom_bindings=False, template="qrprint_navbar.jinja2"    )
		]

	##~~ AssetPlugin
#	def get_assets(self):
#		return dict(
#			js=["js/continuousprint.js"]
#		)


	##~~ Softwareupdate hook
	def get_update_information(self):
		# Define the configuration for your plugin to use with the Software Update
		# Plugin here. See https://docs.octoprint.org/en/master/bundledplugins/softwareupdate.html
		# for details.
		return dict(
			continuousprint=dict(
				displayName="QRprint Plugin",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="heiesch",
				repo="QRprint",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/heiesch/QRprint/archive/{target_version}.zip"
			)
		)
										
										
__plugin_name__ = "QRprint"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = QRprintPlugin()
