
const Contactcard = (props) =>{
    console.log(props.data1)
    return(
        <div className="item">
            <div className="content">
                <div className="header">{props.data1.name}</div>
                <div>{props.data1.email}</div>
            </div>
            <i className="trash alternate outline icon"></i>
        </div>
    );
}
export default Contactcard;