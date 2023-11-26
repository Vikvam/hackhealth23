<script>
    import { onMount } from "svelte";
    import {TextEditor} from "slickgrid";
    import Table from "$lib/components/Table.svelte";

    let mounted = false;
    let columns = [];
    let rows = [];

    async function fetchData() {
        const response = await fetch("http://localhost:8000/biopsy");
        if (response.status > 400) {
            console.log("ERR"); // TODO
            return;
        }
        return response.json();
    }

    function onCellChange(_, args) {
        const biopsy_id = args.item["biopsy_id"];
        const column = args.column.field;
        const change = {[column]: args.item[column]};
        fetch(
            "http://localhost:8000/biopsy/" + biopsy_id,
            {method: "POST", body: JSON.stringify(change), mode: "cors", headers: {"Content-Type": "application/json"}},
        ).then(response => console.log(response));
    }

    onMount(async () => {
        columns = [
            { id: "biopsy_id", name: "Biopsy ID", field: "biopsy_id" },
            // { id: "dg_phir_ids", name: "DG Phir IDs", field: "dg_phir_ids" },
            { id: "projekt", name: "Project", field: "projekt", editor: TextEditor },
            { id: "diagnoza", name: "Diagnosis", field: "diagnoza", editor: TextEditor },
            { id: "onkologicky_kod", name: "Oncology Code", field: "onkologicky_kod", editor: TextEditor },
            { id: "kod_pojistovna", name: "Insurance Code", field: "kod_pojistovna", editor: TextEditor },
            { id: "prijem_lmp", name: "Reception LMP", field: "prijem_lmp", editor: TextEditor },
            { id: "uzavreni_lmp", name: "Closure LMP", field: "uzavreni_lmp", editor: TextEditor },
            { id: "patient_id", name: "Patient ID", field: "patient_id", editor: TextEditor },
            { id: "igv_kontrola", name: "IGV Control", field: "igv_kontrola", editor: TextEditor },
            { id: "medea_zapis", name: "Medea Record", field: "medea_zapis", editor: TextEditor },
            { id: "sekvenator", name: "Sequencer", field: "sekvenator", editor: TextEditor },
            { id: "panel_genu", name: "Gene Panel", field: "panel_genu", editor: TextEditor }, // Dropdown
            { id: "procento_nadorovych_bunek", name: "Percentage of Tumor Cells", field: "procento_nadorovych_bunek", editor: TextEditor },
            { id: "dna_konc_po_1_pcr", name: "DNA Concentration After 1 PCR", field: "dna_konc_po_1_pcr", editor: TextEditor },
            { id: "dna_prum_pokryti", name: "DNA Average Coverage", field: "dna_prum_pokryti", editor: TextEditor },
            { id: "dna_tmb", name: "DNA TMB", field: "dna_tmb", editor: TextEditor },
            { id: "dna_msi", name: "DNA MSI", field: "dna_msi", editor: TextEditor },
            { id: "hrd", name: "HRD", field: "hrd", editor: TextEditor },
            { id: "genom_build_puvodni", name: "Original Genome Build", field: "genom_build_puvodni", editor: TextEditor }
        ];
        rows = await fetchData();
        rows = rows.map((i, idx) => ({id: idx, ...i}));
        console.log(rows);
        mounted = true;
    });
</script>

{#if mounted}
    <Table {columns} {rows} {onCellChange} />
{/if}

