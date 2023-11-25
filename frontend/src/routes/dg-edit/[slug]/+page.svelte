<script>
    import {onMount} from "svelte";
    import {Label} from "flowbite-svelte";
    import {CheckboxFormatter} from "slickgrid";
    import Table from "$lib/components/Table.svelte";

    export let data;
    let slug = data.slug;

    let dgData;

    async function fetchData() {
        const response = await fetch("http://localhost:8000/dg/" + slug);
        if (response.status > 400) {
            console.log("ERR"); // TODO
            return;
        }
        return response.json();
    }

    function renderTable() {

    }

    onMount(async () => {
        // dgData = await fetchData();
        // console.log("DGData", dgData)
    })

    const columns = [
        {id: "title", name: "Title", field: "title"},
        {id: "duration", name: "Duration", field: "duration"},
        {id: "%", name: "% Complete", field: "percentComplete", width: 90},
        {id: "start", name: "Start", field: "start"},
        {id: "finish", name: "Finish", field: "finish"},
        {id: "effort-driven", name: "Effort Driven", field: "effortDriven", formatter: CheckboxFormatter}
    ];
    let rows = [];
    for (let i = 0; i < 50; i++) {
        rows[i] = {
            id: i,
            title: "Task " + i,
            duration: "5 days",
            percentComplete: Math.round(Math.random() * 100),
            start: "01/01/2009",
            finish: "01/05/2009",
            effortDriven: (i % 5 == 0)
        };
    }

</script>

<Label>
    <span>Biopsy ID:</span>
    {slug}
</Label>

<Table columns={columns} rows={rows} />

<style>
    span {
        font-weight: bold;
    }
</style>