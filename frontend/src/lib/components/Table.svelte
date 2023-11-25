<script type="module">
    import { onMount } from "svelte";
    import {
        SlickGrid,
        SlickDataView,
        CheckboxFormatter
    } from "slickgrid";

    let grid;
    let dataView;

    const columns = [
        {id: "title", name: "Title", field: "title"},
        {id: "duration", name: "Duration", field: "duration"},
        {id: "%", name: "% Complete", field: "percentComplete", width: 90},
        {id: "start", name: "Start", field: "start"},
        {id: "finish", name: "Finish", field: "finish"},
        {id: "effort-driven", name: "Effort Driven", field: "effortDriven", formatter: CheckboxFormatter}
    ];
    let columnFilters = {}

    var options = {
        enableCellNavigation: true,
        enableColumnReorder: false,
        showHeaderRow: true,
    };

    let data = [];
    for (let i = 0; i < 50; i++) {
        data[i] = {
            id: i,
            title: "Task " + i,
            duration: "5 days",
            percentComplete: Math.round(Math.random() * 100),
            start: "01/01/2009",
            finish: "01/05/2009",
            effortDriven: (i % 5 == 0)
        };
    }

    function filterTable(item) {
        for (var columnId in columnFilters) {
            if (columnId !== undefined && columnFilters[columnId] !== "") {
                var c = grid.getColumns()[grid.getColumnIndex(columnId)];
                if (item[c.field] != columnFilters[columnId]) return false;
            }
        }
        return true;
    }

    function onFilter(e) {
        const inputFilter = e.target;
        const columnId = inputFilter.dataset.columnid;
        if (columnId != null) {
            columnFilters[columnId] = (e.target.value || '').trim();
            dataView.refresh();
        }
        console.log("onFilter", e.target)
    }

    function renderTable() {
        dataView = new SlickDataView({});
        grid = new SlickGrid("#slickgrid", dataView, columns, options);

        dataView.onRowCountChanged.subscribe(function (e, args) {
            console.log("onRowCountChanged");
            grid.updateRowCount();
            grid.render();
        });

        dataView.onRowsChanged.subscribe(function (e, args) {
            console.log("onRowsChanged");
            grid.invalidateRows(args.rows);
            grid.render();
        });

        grid.onRendered.subscribe((e) => {
            let headerRow = grid.getHeaderRow();
            headerRow.addEventListener("change", onFilter);
            headerRow.addEventListener("keyup", onFilter);
            for (let i = 0; i < headerRow.children.length; i++) {
                const columnId = columns.at(i).id;
                const filterInput = document.createElement('input');
                filterInput.className = 'filter';
                filterInput.placeholder = 'Filter...';
                filterInput.dataset.columnid = columnId;
                filterInput.value = columnFilters[columnId] || '';
                const headerCell = headerRow.childNodes[i];
                headerCell.innerHTML = "";
                headerCell.appendChild(filterInput);
            }
        });

        grid.init();

        dataView.beginUpdate();
        dataView.setItems(data);
        dataView.setFilter(filterTable);
        dataView.endUpdate();
    }

    onMount(async () => {
        renderTable();
    })
</script>

<div id="slickgrid" style="width:100%;height:500px;"></div>

