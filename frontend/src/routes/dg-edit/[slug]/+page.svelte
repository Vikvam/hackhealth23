<script>
    import { onMount } from "svelte";
    import { Label } from "flowbite-svelte";
    import { CheckboxFormatter } from "slickgrid";
    import Table from "$lib/components/Table.svelte";

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

    function onCellChange(args) {
        const fhir_id = args.item["id"];
        const column = args.column.field; // Severity, classification
        // const change = {[column]: args.item[column], fhir_id: fhir_id};
        // console.log(change)
        fetch(
            "http://localhost:8000/classify_dg/?fhir_id=" + fhir_id + "&" + "classification=" + args.item[column],
            {method: "POST", body: JSON.stringify({}), mode: "cors", headers: {"Content-Type": "application/json"}},
        ); //.then(response => console.log(response));
    }

    function insertOptions(selectNode, selected) {
        const options = ["unasigned", "benign", "unknown", "severe"];
        options.forEach(optionText => {
            const option = document.createElement("option");
            option.text = optionText;
            option.value = optionText; // Set the value if needed
            if (selected == optionText) option.selected = true;
            selectNode.appendChild(option);
        });
    }

    function dropdownEditor(args) {
        let $select;
        let defaultValue;
        let scope = this;

        this.init = function () {
            $select = document.createElement("select");
            $select.id = args.item.id;
            $select.addEventListener("change", (e) => {
                args.item[args.column.field] = $select.value;
                onCellChange(args);
            })
            insertOptions($select);
            args.container.appendChild($select);
            $select.focus();
        }

        this.destroy = function () {
            $select.remove();
        };

        this.focus = function () {
            $select.value = item[args.column.field];
        };

        this.loadValue = function (item) {};

        this.applyValue = function(item, state) {};

        this.isValueChanged = function () {};

        this.serializeValue = function () {};

        this.validate = function () {};

        this.init();
    }

    function dropdownFormatter(row, cell, value, columnDef, dataContext) {
        let span = document.createElement("span");
        span.innerText = value;
        span.classList.add("classification");
        span.classList.add("classification-" + value);
        // let grid = document.querySelector("#dg-table .slick-viewport .grid-canvas");
        // if (grid && grid.childNodes[row]) {
        //     grid.childNodes[row].classList.add("classification-" + value);
        // }
        return span;
    }

    onMount(async () => {
        columns = [
            {id: "classification", name: "Severity", field: "classification", editor: dropdownEditor, formatter: dropdownFormatter},
            // {id: "id", name: "id", field: "id"},
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
        rows = rows.map(i => ({"Severity": "unknown", ...i}));
        mounted = true;

        // setTimeout(() => {
        //     let grid = document.querySelector("#dg-table .slick-viewport .grid-canvas");
        //     for (let i = 0; i < grid.children.length; i++) {
        //         grid.childNodes[i].classList.add("classification-" + grid.childNodes[i].firstChild.firstChild.innerText)
        //     }
        // }, 150);
    });
</script>

<Label>
    <span class="mb-4">Biopsy ID:</span>
    {slug}
</Label>

{#if mounted}
    <Table {columns} {rows} tableId="dg-table"/>
{/if}

<style>
    span {
        font-weight: bold;
    }
    :global(.classification) {
        display: inline-block;
        width: 100%;
    }
    :global(.classification-unasigned) {
        background-color: white !important;
    }
    :global(.classification-benign) {
        background-color: lightgreen !important;
    }
    :global(.classification-unknown) {
        background-color: palegoldenrod !important;
    }
    :global(.classification-severe) {
        background-color: lightcoral !important;
    }
</style>
