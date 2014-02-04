import sublime, sublime_plugin, time

class InsertDatetimeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
	format = "%Y-%m-%d %H.%M:%S"
        sel = self.view.sel();
        for s in sel:
	    if s.empty():
                self.view.insert(edit, s.a, strftime(format, localtime()))
	    else:
                self.view.replace(edit, s, strftime(format, localtime()))
