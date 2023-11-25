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
        {
            id: "Chromosome",
            name: "Chromosome",
            field: "Chromosome",
            width: 100,
        },
        { id: "Region", name: "Region", field: "Region", width: 150 },
        { id: "Type", name: "Type", field: "Type", width: 100 },
        { id: "Reference", name: "Reference", field: "Reference", width: 150 },
        { id: "Allele", name: "Allele", field: "Allele", width: 100 },
        { id: "Length", name: "Length", field: "Length", width: 100 },
        { id: "Count", name: "Count", field: "Count", width: 100 },
        { id: "Coverage", name: "Coverage", field: "Coverage", width: 100 },
        { id: "Frequency", name: "Frequency", field: "Frequency", width: 100 },
        {
            id: "ForwardReverseBalance",
            name: "Forward Reverse Balance",
            field: "Forward Reverse Balance",
            width: 150,
        },
        {
            id: "AverageQuality",
            name: "Average Quality",
            field: "Average Quality",
            width: 150,
        },
        { id: "GeneName", name: "Gene Name", field: "Gene Name", width: 150 },
        {
            id: "CodingRegionChange",
            name: "Coding Region Change",
            field: "Coding Region Change",
            width: 200,
        },
        {
            id: "AminoAcidChange",
            name: "Amino Acid Change",
            field: "Amino Acid Change",
            width: 150,
        },
        {
            id: "ExonNumber",
            name: "Exon Number",
            field: "Exon Number",
            width: 150,
        },
        {
            id: "TypeOfMutation",
            name: "Type of Mutation",
            field: "Type of Mutation",
            width: 150,
        },
    ];
        rows = (await fetchData()).dg;
        mounted = true;
    });
</script>

{#if mounted}
    <Table {columns} {rows} />
{/if}

<style>
    /* Add any custom styling for your table */
    #myGrid {
        width: 100%;
        height: 500px;
    }
</style>
