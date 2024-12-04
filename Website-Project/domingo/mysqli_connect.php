<?php
$dbcon = @mysqli_connect('localhost', 'vashtidomingo', 'vashtidomingo', 'members_domingo')
OR die('>> Could not connect to the MySQL Server: ' . mysqli_connect_error() . ':(');
mysqli_set_charset($dbcon, 'utf8');