#!/bin/bash

REP_STRAT="'SimpleStrategy'"
REP_FACTOR=2
SQL_STR="CREATE KEYSPACE IF NOT EXISTS $2 WITH REPLICATION = {'class' : $REP_STRAT, 'replication_factor' : $REP_FACTOR};"

cqlsh $1 << EOF
$SQL_STR
EOF
