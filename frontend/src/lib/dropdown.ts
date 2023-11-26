export function insertOptions(selectNode, selected) {
    const options = ["unasigned", "benign", "unknown", "severe"];
    options.forEach(optionText => {
        const option = document.createElement("option");
        option.text = optionText;
        option.value = optionText; // Set the value if needed
        if (selected == optionText) option.selected = true;
        selectNode.appendChild(option);
    });
}

export function dropdownEditor(args) {
    let $select;
    let defaultValue;
    let scope = this;

    this.init = function () {
        $select = document.createElement("select");
        $select.id = args.item.id;
        $select.addEventListener("change", (e) => {
            args.item[args.column.field] = $select.value}
        )
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

export function dropdownFormatter(row, cell, value, columnDef, dataContext) {
    console.log(row, cell, value)
    let select = document.createElement("select");
    insertOptions(select);
    return select;
}

