import React from "react";

export default class BckBtn extends React.Component {

    goBack() {
        console.log("in")
        window.history.go(-1)

    }


    render() {
        <button className='back-btn' onClick={this.goBack.bind(this)}>Back</button>

    }

}
