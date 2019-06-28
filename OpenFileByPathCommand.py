import sublime
import sublime_plugin
import os
import subprocess

class OpenFileByPathCommand(sublime_plugin.WindowCommand):
  def run(self):
    def done_callback(path):
      if os.path.isdir(path):
        self.open_in_new_window(path)
      else:
        self.open_file(path)

    self.window.show_input_panel("Open File by Path: ", "", done_callback, None, None)

  def open_file(self, path):
    self.window.open_file(path)

  def open_in_new_window(self, path):
    if sublime.platform() == 'osx':
      try:
        subprocess.Popen(['subl', '.'], cwd=path)
      except:
        try:
          subprocess.Popen(['sublime', '.'], cwd=path)
        except:
          subprocess.Popen(['/Applications/Sublime Text 3.app/Contents/SharedSupport/bin/subl', '.'], cwd=path)
    elif sublime.platform() == 'windows':
      try:
        subprocess.Popen(['subl', '.'], cwd=path, shell=True)
      except:
        try:
          subprocess.Popen(['sublime', '.'], cwd=path, shell=True)
        except:
          try:
            subprocess.Popen(['sublime_text', '.'], cwd=path, shell=True)
          except:
            subprocess.Popen(['C:/Program Files/Sublime Text 3/sublime_text.exe', '.'], cwd=path, shell=True)
    else:
      try:
        subprocess.Popen(['subl', '.'], cwd=path)
      except:
        subprocess.Popen(['sublime', '.'], cwd=path)
