<script>
    import { onMount } from "svelte";
    import { SlickGrid, CheckboxFormatter } from "slickgrid";

    let data = [];
    let grid;

    let columns = [
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

    var options = {
        enableCellNavigation: true,
        enableColumnReorder: false,
    };

    onMount(async () => {
        const response = await fetch("http://localhost:8000/dg");
        const result = await response.json();
        data = result.dg;

        // Initialize SlickGrid with the retrieved data
        grid = new SlickGrid("#myGrid", data, columns, options);
    });
</script>

<div id="myGrid" />

<style>
    /* Add any custom styling for your table */
    #myGrid {
        width: 100%;
        height: 500px;
    }
</style>
