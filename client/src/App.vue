<template>
  <div id="app">
    <Header />
    <router-view></router-view>
    <Footer />
  </div>
</template>

<script>
import Header from './components/layouts/Header'
import Footer from './components/layouts/Footer'

export default {
  name: 'app',
  components: {
    Header,
    Footer
  },
  created () {
      document.title = "wortex";
  }
}
</script>

<style>
  body {
    background-color: #272727;
    color: #FFE400;
    margin: 0px;
  }
  main{
    margin: 30px;
  }
  .table th {
    border-spacing: 0px;
    padding: 0px;
    font-size: 11px;
    text-align: center;
  }
  .table td {
    border-spacing: 0px;
    padding: 0px;
    font-size: 11px;
    text-align: left;
  }
  .col-sm {
    width: 45px;
  }
  .col-long {
    width: 800px;
  }
  .thumb_img {
    width: 100%;
  }
  .hover_img a {
    position:relative;
    font-size: 11px;
    color: #FF652F;
    text-decoration: none;
  }
  .hover_img a span {
    position:absolute;
    display:none;
    z-index:99;
  }
  .hover_img td:hover span{
    display:block;
    position:fixed;
    left :51%;
    top: 50%;
    transform: translate(-1%, -50%);
  }
  .gray-txt{
    color: #747474;
  }
  .green-txt{
    color: #14A76C;
    margin: 0;
  }
  .footer {
    position: relative;
    bottom: 0;
    width: 100%;
    color: #747474;
    text-align: center;
  }
  #submit {
    border: 0;
    border-spacing: 0px;
    padding: 0px;
  }
  .nav-link:hover {
    color: #14A76C;
  }
  .nav-link {
    color: #747474;
  }
  .btn-secondary {
    color: #272727;
  }
  .btn-secondary:hover {
    color: #14A76C;
  }
  input[type=text] {
    background-color: #6c757d;
    width: 250px;
    height: 30px;
    border: none;
    border-radius: 1px;
  }
  input[type=text]:focus {
    border: 1px solid #272727;
  }
  input::placeholder {
    color: #272727;
  }
  #menu{
    list-style-type:none;
    margin:0px;
    padding:0px;
    position: absolute;
    display: table;
  }
  #menu li {
    display: table-cell;
    margin-right: 1px;
  }
  .menu-item {
    margin-top: 0px;
  }
  .menu-item a {
    color: #6c757d;
  }
  .menu-item a:hover {
    color: #14A76C;
    text-decoration: none;
  }
  #menu li + li:before {
    padding: 5px;
    color: #ccc;
    content: "/\00a0";
  }
  .articles {
    color: #FF652F;
    margin: 4px 0 0;
  }
  .articles a {
    color: #FF652F;
  }
  .articles a:hover {
    color: #14A76C;
    text-decoration: none;
  }
  .articles li p{
    font-size: 11px;
    margin: 0 0 0;
    color: #747474;
  }
  .success {
    width: 15%;
    height: 15px;
    margin-left:auto;
    margin-right:0;
  }

</style>