import interpreter
from interpreter import*

tokens [0] == 'Print'
command_line [1] == 'Print'

func_name = tokens[0]
function = [func_name] = ' join '

string [0] == ' any '
command_line [1] == ' any '

func_name = tokens[0]
function = [func_name] = ' join '

string [0] == ' Hello World '
command_line [1] == 'Print'

func_name = tokens[0]
function = [func_name] = ' join '

string [0] == ' Good Bye World '
command_line [1] == ' Print '

func_name = tokens[0]
function = [func_name] = ' join '

tokens [0] == 'Import'
command_line [1] == 'Import'

func_name = tokens[0]
function = [func_name] = 'join'

string [0] == ' OS '
command_line[1] == ' Import '

string [0] == ' SYS '
command_line [1] == ' Import '

func_name = tokens[0]
function = [func_name] = ' join '

tokens [0] == ' BIT '
command_line[1] == ' BIT '

func_name = tokens[0]
function = [func_name] = ' join '

string [0] == ' 16 '
command_line[1] == ' BIT '

func_name = tokens[0]
function = [func_name] = ' join '

string [0] == ' How are you? '
command_line[1] == ' Print '

func_name = tokens[0]
function = [func_name] = ' join '

tokens [0] == ' input '
command_line[1] == ' input() '

func_name = tokens[0]
funciton = [func_name] = ' join '

string [0] == ' I am good. '
command_line == ' input '

func_name = tokens[0]
function = [func_name] = ' join '

tokens[0] == 'Class'
command_line == ' Class (): '

func_name = tokens[0]
function = [func_name] = ' join '

string [0] == ' any '
command_line == ' Class (): '

func_name = tokens[0]
function = [func_name] = ' join '

tokens[0] == 'Question'
command_line == ' Question() '

func_name = tokens[0]
function = [func_name] = ' join '

string [0] == '10 * 2 + 2'
command_line == ' Question(10 * 2 + 2) '

func_name = tokens[0]
function = [func_name] = ' join '

tokens[0] == ' Null '
command_line == ' null '

func_name = tokens[0]
function = [func_name] = ' join '