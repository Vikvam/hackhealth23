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
        $select.addEventListener("change", (e) => console.log($select.value))
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

    this.loadValue = function (item) {
        console.log("loadValue")
        $select.value = defaultValue;
        $select.focus();
    };

    this.applyValue = function(item, state) {
        console.log("applyValue", args.column.field, item, state)
        $select.value = state;
    };

    this.isValueChanged = function () {
        console.log("isValueChanged")
        return ($select.value != defaultValue);
    };

    this.serializeValue = function () {
        console.log("serializeValue →", $select.value)
        return $select.value;
    };

    this.validate = function () {
        return {
            valid: true,
            msg: null
        };
    };

    this.init();
}

export function dropdownFormatter(row, cell, value, columnDef, dataContext) {
    console.log(row, cell, value)
    let select = document.createElement("select");
    insertOptions(select);
    return select;
}

