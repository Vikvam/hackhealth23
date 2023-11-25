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
        // Add more columns based on your data
    ];

    var options = {
        enableCellNavigation: true,
        enableColumnReorder: false,
    };

    onMount(async () => {
        const response = await fetch("http://localhost:8000/dg", {mode: "cors"});
        const result = await response.json();
        data = result.dg;

        // Initialize SlickGrid with the retrieved data
        grid = new Slick.Grid("#myGrid", data, columns, options);
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
