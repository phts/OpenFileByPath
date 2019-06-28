import sublime
import sublime_plugin

class OpenFileByPathCommand(sublime_plugin.WindowCommand):
  def run(self):
    def done_callback(path):
      self.open_file(path)

    self.window.show_input_panel("Open File by Path: ", "", done_callback, None, None)

  def open_file(self, path):
    self.window.open_file(path)
