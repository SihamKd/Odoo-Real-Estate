/** @odoo-module **/

import { Component , useState, onWillUnmount} from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { FormView } from "@app_one/components/formView/formView";

export class ListViewAction extends Component {
    static template = "app_one.ListView";
    static components = {FormView};

    setup() {
        this.state = useState({
            'records': [],
        });
        this.orm = useService("orm");
        this.rpc = useService("rpc");
        this.loadRecords();

        this.intervalId = setInterval(() => {this.loadRecords()},3000);

        this.onRecordCreated = this.onRecordCreated.bind(this);
        
        onWillUnmount(() => {
            clearInterval(this.intervalId);
        });
    }

    // async loadRecords() {
    //     const result = await this.orm.searchRead("property", [], []);
    //     console.log("Records from property model:", result);
    //     this.state.records = result;
    // };

    async loadRecords() {
        const result = await this.rpc("/web/dataset/call_kw", {
            model: "property",
            method: "search_read",
            args: [[]],
            kwargs: {fields: ['id', 'name', 'postcode', 'date_availability']},
        });
        console.log("Records from property model:", await result);
        this.state.records = result;
    };    

    async createRecord() {
        await this.rpc("/web/dataset/call_kw", {
            model: "property",
            method: "create",
            args: [{
                name: "New Property",
                description: "A newly created property",
                postcode: "00000",
                bedrooms: 2,
                date_availability: "2023-12-01",
            }],
            kwargs: {},
        })
        this.loadRecords();

    };


    async deleteRecord(recordId) {
        await this.rpc("/web/dataset/call_kw", {
            model: "property",
            method: "unlink",
            args: [recordId],
            kwargs: {},
        });
        this.loadRecords();
    }

    toggleCreateForm() {
        console.log("Inside toggleCreateForm method");
        this.state.showCreateForm = !this.state.showCreateForm;
        console.log("showCreateForm state:", this.state.showCreateForm);
    }
    
    onRecordCreated() {
        this.loadRecords();
        this.state.showCreateForm = false;
    }
}   


registry.category("actions").add("app_one.action_list_view", ListViewAction);
