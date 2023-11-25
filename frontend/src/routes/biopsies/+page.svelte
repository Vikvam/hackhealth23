<script>
    import { onMount } from "svelte";
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

    onMount(async () => {
        columns = [
            { id: "biopsy_id", name: "Biopsy ID", field: "biopsy_id" },
            { id: "dg_phir_ids", name: "DG Phir IDs", field: "dg_phir_ids" },
            { id: "projekt", name: "Project", field: "projekt" },
            { id: "diagnoza", name: "Diagnosis", field: "diagnoza" },
            { id: "onkologicky_kod", name: "Oncology Code", field: "onkologicky_kod" },
            { id: "kod_pojistovna", name: "Insurance Code", field: "kod_pojistovna" },
            { id: "prijem_lmp", name: "Reception LMP", field: "prijem_lmp" },
            { id: "uzavreni_lmp", name: "Closure LMP", field: "uzavreni_lmp" },
            { id: "patient_id", name: "Patient ID", field: "patient_id" },
            { id: "igv_kontrola", name: "IGV Control", field: "igv_kontrola" },
            { id: "medea_zapis", name: "Medea Record", field: "medea_zapis" },
            { id: "sekvenator", name: "Sequencer", field: "sekvenator" },
            { id: "panel_genu", name: "Gene Panel", field: "panel_genu" },
            { id: "procento_nadorovych_bunek", name: "Percentage of Tumor Cells", field: "procento_nadorovych_bunek" },
            { id: "dna_konc_po_1_pcr", name: "DNA Concentration After 1 PCR", field: "dna_konc_po_1_pcr" },
            { id: "dna_prum_pokryti", name: "DNA Average Coverage", field: "dna_prum_pokryti" },
            { id: "dna_tmb", name: "DNA TMB", field: "dna_tmb" },
            { id: "dna_msi", name: "DNA MSI", field: "dna_msi" },
            { id: "hrd", name: "HRD", field: "hrd" },
            { id: "genom_build_puvodni", name: "Original Genome Build", field: "genom_build_puvodni" }
        ];
        rows = await fetchData();
        rows = rows.map(i => ({id: i.biopsy_id, ...i}));
        console.log(rows);
        mounted = true;
    });
</script>

{#if mounted}
    <Table {columns} {rows} />
{/if}

