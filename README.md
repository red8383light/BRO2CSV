# BRO2CSV
Bro2csv is desinged to turn BRO data in a file into a csv formatted file.


This is a pure Python implementation.

To install bro2csv, simply run './configure'.

The header.py file will need to be updated periodically.
This is due to changes within bro starting at 2.4 where certain column names where changed.
Furthermore, it will need to be updated for other headers not currently
in the header.py or custom headers of your own.

To add a new header, you can do a HEAD of the particular log file and grab the header line.
Then comma separate each column name and add to header.py following the format:
(file name without the '.log)="comma separated column names"

Example:

example="try,this,example"
