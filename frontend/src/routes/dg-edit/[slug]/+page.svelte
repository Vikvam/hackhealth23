<script>
    import { onMount } from "svelte";
    import { Label } from "flowbite-svelte";
    import { CheckboxFormatter } from "slickgrid";
    import Table from "$lib/components/Table.svelte";
    import { SelectCellEditor, SelectCellFormatter} from "$lib/dropdown.ts";

    export let data;
    let slug = data.slug;

    let mounted = false;
    let columns = [];
    let rows = [];

    async function fetchData() {
        const response = await fetch("http://localhost:8000/dg/" + slug);
        if (response.status > 400) {
            console.log("ERR"); // TODO
            return;
        }
        return response.json();
    }

    let severityList = {
        "1": "Low",
        "2": "Medium",
        "3": "High",
    };

    onMount(async () => {
        columns = [
            {id: "Severity", name: "Severity", field: "Severity",  formatter: SelectCellFormatter, options: severityList},
            {id: "id", name: "id", field: "id"},
            {id: "Biopsy ID", name: "Biopsy ID", field: "Biopsy ID"},
            {id: "Chromosome", name: "Chromosome", field: "Chromosome"},
            {id: "Region", name: "Region", field: "Region"},
            {id: "Type", name: "Type", field: "Type"},
            {id: "Reference", name: "Reference", field: "Reference"},
            {id: "Allele", name: "Allele", field: "Allele"},
            {id: "Length", name: "Length", field: "Length"},
            {id: "Count", name: "Count", field: "Count"},
            {id: "Coverage", name: "Coverage", field: "Coverage"},
            {id: "Frequency", name: "Frequency", field: "Frequency"},
            {id: "ForwardReverseBalance", name: "Forward Reverse Balance", field: "Forward Reverse Balance"},
            {id: "AverageQuality", name: "Average Quality", field: "Average Quality"},
            {id: "GeneName", name: "Gene Name", field: "Gene Name"},
            {id: "CodingRegionChange", name: "Coding Region Change", field: "Coding Region Change"},
            {id: "AminoAcidChange", name: "Amino Acid Change", field: "Amino Acid Change"},
            {id: "ExonNumber", name: "Exon Number", field: "Exon Number"},
            {id: "TypeOfMutation", name: "Type of Mutation", field: "Type of Mutation"},
        ];
        rows = (await fetchData()).dg;
        mounted = true;
    });
</script>

<Label>
    <span>Biopsy ID:</span>
    {slug}
</Label>

{#if mounted}
    <Table {columns} {rows} />
{/if}

<style>
    span {
        font-weight: bold;
    }
</style>
