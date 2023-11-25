<script>
    import { onMount } from "svelte";
    import Table from "$lib/components/Table.svelte";

    let mounted = false;
    let columns = [];
    let rows = [];

    async function fetchData() {
        const response = await fetch("http://localhost:8000/dg");
        if (response.status > 400) {
            console.log("ERR"); // TODO
            return;
        }
        return response.json();
    }

    onMount(async () => {
        columns = [
            { id: "Chromosome", name: "Chromosome", field: "Chromosome" },
            { id: "Region", name: "Region", field: "Region" },
            { id: "Type", name: "Type", field: "Type" },
            { id: "Reference", name: "Reference", field: "Reference" },
            { id: "Allele", name: "Allele", field: "Allele" },
            { id: "Length", name: "Length", field: "Length" },
            { id: "Count", name: "Count", field: "Count" },
            { id: "Coverage", name: "Coverage", field: "Coverage" },
            { id: "Frequency", name: "Frequency", field: "Frequency" },
            {
                id: "ForwardReverseBalance",
                name: "Forward Reverse Balance",
                field: "Forward Reverse Balance",
            },
            {
                id: "AverageQuality",
                name: "Average Quality",
                field: "Average Quality",
            },
            { id: "GeneName", name: "Gene Name", field: "Gene Name" },
            {
                id: "CodingRegionChange",
                name: "Coding Region Change",
                field: "Coding Region Change",
            },
            {
                id: "AminoAcidChange",
                name: "Amino Acid Change",
                field: "Amino Acid Change",
            },
            { id: "ExonNumber", name: "Exon Number", field: "Exon Number" },
            {
                id: "TypeOfMutation",
                name: "Type of Mutation",
                field: "Type of Mutation",
            },
        ];
        rows = (await fetchData()).dg;
        mounted = true;
    });
</script>

<style>
.grid-container {
    display: grid;
    grid-template-columns: auto auto auto; /* Adjust this to change the number of columns */
    gap: 10px; /* Adjust this to change the gap between the grid items */
    padding: 10px; /* Adjust this to change the padding around the grid */
}

.grid-container > div {
    background-color: #f1f1f1;
}
</style>

{#if mounted}
    <div class="grid-container">
        <div><Table tableId="table1" {columns} {rows} heightStyle="200px" usePager={false}/></div>
        <div><Table tableId="table2" {columns} {rows} heightStyle="200px" usePager={false}/></div>
        <div><Table tableId="table3" {columns} {rows} heightStyle="200px" usePager={false}/></div>
        <div><Table tableId="table4" {columns} {rows} heightStyle="200px" usePager={false}/></div>
    </div>
{/if}
