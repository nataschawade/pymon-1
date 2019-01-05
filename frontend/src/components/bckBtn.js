import React from "react";

export default class BckBtn extends React.Component {
    constructor(props){
        super(props);
    }

    render(){
        return(
        <div className="back-btn">
        <a href="../games">Back to games page</a>
        </div>
    )

    }

}