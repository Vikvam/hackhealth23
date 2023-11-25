<script type="module">
    import {
        SlickGrid,
        CheckboxFormatter,
    } from "slickgrid";

    let grid;
    // let dataView = new DataView({inlineFilters: true});

    const columns = [
        {id: "title", name: "Title", field: "title"},
        {id: "duration", name: "Duration", field: "duration"},
        {id: "%", name: "% Complete", field: "percentComplete", width: 90},
        {id: "start", name: "Start", field: "start"},
        {id: "finish", name: "Finish", field: "finish"},
        {id: "effort-driven", name: "Effort Driven", field: "effortDriven", formatter: CheckboxFormatter}
    ];

    console.log(CheckboxFormatter)

    var options = {
        enableCellNavigation: true,
        enableColumnReorder: false,
    };

    let data = [];
    for (let i = 0; i < 50; i++) {
        data[i] = {
            title: "Task " + i,
            duration: "5 days",
            percentComplete: Math.round(Math.random() * 100),
            start: "01/01/2009",
            finish: "01/05/2009",
            effortDriven: (i % 5 == 0)
        };
    }

    function renderTable() {
        grid = new SlickGrid("#slickgrid", data, columns, options);
    }
</script>

<div id="slickgrid" style="width:100%;height:500px;"></div>

<svelte:window on:load={renderTable}></svelte:window>
