#sed comment – This script deletes unnecessary parts of TKR-doc files

#delete first n lines
#/^E/ s/.*//
#delete empty lines
/^$/d
#delete lines with patterns (from, to)
/Staatsarchiv des Kantons Zürich/,/Datum/ s/.*//
#delete lines with patterns (from, to the end)
/\[Transkript/,/$/ s/.*//
#delete lines with patterns (from, to the end)
/PAGE/,/$/ s/.*//