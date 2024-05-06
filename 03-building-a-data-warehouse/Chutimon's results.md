# Building a Data Warehouse
Name : Chutimon Cherdpongtagit
ID : 66199160146

- Add more tables at def main(dataset_id, table_id, file_path)
such as
bigquery.SchemaField("actor", bigquery.SqlTypeNames.STRING),
bigquery.SchemaField("repo", bigquery.SqlTypeNames.STRING),
bigquery.SchemaField("create_at", bigquery.SqlTypeNames.STRING),
bigquery.SchemaField("payload", bigquery.SqlTypeNames.STRING),

- The problem : I can't figure out how to add subtables to each table. 
Because when I try to add more subtables, it will get the error.
-> Error : 
                    writer.writerow([
                        each["id"], 
                        each["type"],
                        each["actor"]["id"],
                        each["actor"]["name"],
                        each["repo"]["id"],
                        each["repo"]["name"],
                        each["created_at"],
                        each["payload"],
                        ])

-> No error :
                    writer.writerow([
                        each["id"], 
                        each["type"],
                        each["actor"]["id"],
                        each["repo"]["id"],
                        each["created_at"],
                        each["payload"],
                        ])
