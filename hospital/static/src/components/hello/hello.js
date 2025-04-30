/** @odoo-module **/

import { Component } from "@odoo/owl";

export class HelloWorld extends Component {
  static template = "hospital.HelloWorldTemplate";

  setup() {
    this.greeting = "Halo dari OWL!";
  }
}
