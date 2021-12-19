#!/bin/bash
bench init frappe-bench
cd ./frappe-bench
bench new-app --no-git scouts
bench new-site scouts.erp.local --db-type postgres --db-host 127.0.0.1
cd ../
./test.sh
cd ./frappe-bench
bench --site scouts.erp.local install-app scouts
bench --site scouts.erp.local set-config --global developer_mode 1
