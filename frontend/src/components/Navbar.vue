<template>
  <b-navbar toggleable="md" type="light" variant="light">
    <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
    <b-navbar-brand href="#">NavBar</b-navbar-brand>
    <b-collapse is-nav id="nav_collapse">
      <b-navbar-nav>
        <b-nav-item :to="{'name': 'index'}">Home</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>