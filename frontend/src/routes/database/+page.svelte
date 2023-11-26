<script>
    import { onMount } from "svelte";
    import Table from "$lib/components/Table.svelte";

    let mounted = false;
    let columnsGeneDanger = [];
    let columns = [];
    let rowsGeneDanger = [];
    let rows = [];

    async function fetchData() {
        const response = await fetch("http://localhost:8000/geneDanger");
        if (response.status > 400) {
            console.log("ERR"); // TODO
            return;
        }
        return response.json();
    }

    function linkFormatter(row, cell, value, columnDef, dataContext) {
        console.log(value)
        return "<a style='color: blue; text-decoration: underline' href='http://www.google.com/search?q=" + value + "' target='_blank'>" + value + "</a>";
    }

    onMount(async () => {
        columnsGeneDanger = [
            { id: "name", name: "Gene", field: "name", formatter: linkFormatter },
            { id: "n_safe", name: "# Pathogenic", field: "n_safe" },
            { id: "n_dangerous", name: "# Benign", field: "n_dangerous" },
            { id: "freq", name: "% Freq", field: "freq" },
        ];
        rowsGeneDanger = (await fetchData());
        console.log(rowsGeneDanger)
        mounted = true;
    });
</script>

<style>
.grid-container {
    display: grid;
    grid-template-columns: auto auto auto; /* Adjust this to change the number of columns */
    gap: 10px; /* Adjust this to change the gap between the grid items */
    padding: 10px; /* Adjust this to change the padding around the grid */
    width: 100%;
}

.grid-container > div {
    background-color: #f1f1f1;
    width: 100%;
}
</style>

{#if mounted}
    <div class="grid-container">
        <div><Table tableId="table1" columns={columnsGeneDanger} rows={rowsGeneDanger} options={{defaultColumnWidth: 30}} heightStyle="350px" usePager={true}/></div>
        <div><Table tableId="table2" {columns} {rows} heightStyle="200px" usePager={true}/></div>
        <div><Table tableId="table3" {columns} {rows} heightStyle="200px" usePager={true}/></div>
        <div><Table tableId="table4" {columns} {rows} heightStyle="200px" usePager={true}/></div>
    </div>
{/if}
