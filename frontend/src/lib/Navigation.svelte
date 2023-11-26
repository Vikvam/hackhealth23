<script>
    import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from "flowbite-svelte";
</script>

<Navbar fluid=true >
  <NavBrand href="/">
    <img src="/logo.png" class="h-6 sm:h-16" alt="Flowbite Logo" />
    <span id="name" class="self-center whitespace-nowrap lg:text-xl font-bold dark:text-white">CzechGEN</span>
  </NavBrand>
  <NavHamburger  />
  <NavUl >
    <NavLi href="/">Home</NavLi>
    <NavLi href="/upload">Upload DG</NavLi>
    <NavLi href="/biopsies">CLC</NavLi>
    <NavLi href="/mutations">Mutations</NavLi>
    <NavLi href="/database">Overview</NavLi>
    <NavLi href="/settings">Settings</NavLi>
  </NavUl>
</Navbar>

<style>
  #name {
    font-size: 1.5em;
  }
</style>