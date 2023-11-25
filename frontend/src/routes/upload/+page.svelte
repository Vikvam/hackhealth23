<script>
    import {goto} from "$app/navigation.js";
    import {Fileupload, Helper, Input, Label, Button, Heading} from "flowbite-svelte";

    let id;
    let filepath;

    function uploadFile() {
        const fileUpload = document.getElementById("file-upload");
        if (! fileUpload.files) return;
        const file = fileUpload.files[0];
        const name = file.name.slice(0, file.name.lastIndexOf('.'));
        const formData = new FormData();
        formData.append("name", name);
        formData.append("file", file);
        fetch(
            "http://localhost:8000/uploadxlsx/?name=" + id,
            {method: "POST", body: formData, mode: "cors"},
        ).then(response => console.log(response));
        // goto("/dg-edit", {replaceState: false});
    }
</script>

<div>
  <Heading tag="h3" class="space-y-10 mb-4">Insert new biopsy</Heading>
  <!--  TODO: validation-->
  <Label class="space-y-4 mt-4 mb-4">
    <span>Biopsy ID</span>
    <Input bind:value={id} />
  </Label>
  <Label class="space-y-4 mt-4 mb-4">
    <span>DG file</span>
    <Fileupload id="file-upload" bind:value={filepath} />
    <Helper>Excel files</Helper>
    <Helper>File: {filepath ? filepath : "No file uploaded"}</Helper>
  </Label>
  <Button on:click={uploadFile} class="mt-4">Insert into database</Button>
</div>

<style>
  div {
    display: grid;
  }
  span {
    font-weight: bold;
  }
</style>
