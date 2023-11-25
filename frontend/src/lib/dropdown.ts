function onchange() {
    console.log("bla")
}

export function SelectCellFormatter(row, cell, value, columnDef, dataContext) {
    console.log("value", value)
    return `<select class='editor-select'>
                <option value=''>Severity...</option>
                <option value='Benign'>Benign</option>
                <option value='Unknown'>Unknown</option>
                <option value='Dangerous'>Dangerous</option>
            </select>`;
}

export function SelectCellEditor(args) {
    var select = document.createElement('select');
    select.className = 'editor-select';
    select.innerHTML = "<option value=''>Select...</option><option value='Option1'>Option1</option><option value='Option2'>Option2</option>";
    select.value = args.item[args.column.field];
    select.addEventListener('change', function () {
        args.commitChanges();
    });

    this.init = function () {
        args.container.appendChild(select);
    };

    this.destroy = function () {
        select.remove();
    };

    this.focus = function () {
        select.focus();
    };

    this.loadValue = function (item) {
        select.value = item[args.column.field];
    };

    this.serializeValue = function () {
        return select.value;
    };

    this.applyValue = function (item, state) {
        item[args.column.field] = state;
    };

    this.isValueChanged = function () {
        return select.value != args.item[args.column.field];
    };

    this.validate = function () {
        return {
            valid: true,
            msg: null
        };
    };

    this.init();
}
