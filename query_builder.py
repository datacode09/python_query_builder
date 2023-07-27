def generate_queries(filename, schema_names, table_names, num_partitions):
    with open(filename, 'w') as file:
        for schema_name in schema_names:
            for table_name in table_names:
                for partition in range(1, num_partitions + 1):
                    query = "SELECT COUNT(*) FROM {}.{}(IDB_PARTITION_{});".format(
                        schema_name, table_name, partition
                    )
                    file.write(query + " UNION ALL\n")

if __name__ == "__main__":
    file_name = "queries.txt"
    schema_names = ["schema1", "schema2", "schema3"]  # Replace with actual schema names
    table_names = ["table1", "table2", "table3"]  # Replace with actual table names
    num_partitions = 14
    generate_queries(file_name, schema_names, table_names, num_partitions)
    print(f"Queries have been generated and saved in '{file_name}'")
