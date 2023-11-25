<script type="module">
    import { onMount } from "svelte";
    import {
        SlickGrid,
        SlickDataView
    } from "slickgrid";

    export let columns;
    export let rows;

    let grid;
    let dataView;

    let columnFilters = {}

    var options = {
        enableCellNavigation: true,
        enableColumnReorder: false,
        showHeaderRow: true,
    };

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
        const parent = inputFilter.parentNode;
        const columnId = inputFilter.dataset.columnid;
        if (columnId != null) {
            columnFilters[columnId] = (e.target.value || '').trim();
            dataView.refresh();
            setTimeout(() => {
                parent.firstElementChild.focus();
            }, 10)
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
            //remove first row from args.rows
            console.log("onRowsChanged", args.rows);
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
        dataView.setItems(rows);
        dataView.setFilter(filterTable);
        dataView.endUpdate();
    }

    onMount(async () => {
        renderTable();
    })
</script>

<div id="slickgrid" style="width:100%;height:500px;"></div>

