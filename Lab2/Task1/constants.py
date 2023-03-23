DECLARATIVE_PATTERN = "(?<![A-Z])(?<!Dr)(?<!Mr)(?<!Mrs)(?<!Ave)(?<!Blvd)(?<!Ln)(?<!Rd)(?<!Inc)(\.+|\!+\?+|\?+\!+|\?+|\!+)"
TWO_WORDS_ABBREVIATIONS = ['e.g.', 'i.e.', 'p.s.', 'ph.d.', 'a.m.', 'p.m.']
NON_DECLARATIVE_PATTERN = "(\!+\?+|\?+\!+|\?+|\!+)"
WORD_PATTERN = r'\b\w+\b'  # including only nums
NUMBER_PATTERN = r'\b\d+\b'
