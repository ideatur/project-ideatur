import React, { Fragment } from "react";
import './easy-form.css';

class EasyForm extends React.Component {
    state = {

    }
    render() {
        return (
            <Fragment>
                <div className="main-form">
                    <h1 className="form-title">Топ-10 найкращих сімейних готелів Єгипту →</h1>
                    <form className="search-hotel">
                        <div className="form-wrapper">

                            <div className="form-div">
                                <label>Країна, місто, готель</label>
                                <input type="text" name="country" placeholder="Туреччина"></input>
                            </div>

                            <div className="form-div">
                                <label>Місто вильоту</label>
                                <input type="text" name="country" placeholder=""></input>
                            </div>

                            <div className="form-div">
                                <label>Дата вильоту</label>
                                <input type="date" name="country" value="2020-01-01"
                                        max="2030-01-01" min="2020-01-01" className="form-date"></input>
                            </div>

                            <div className="form-div">
                            <label>Кількість ночей</label>
                                <input type="text" name="country" placeholder=""></input>
                            </div>

                            <div className="form-div">
                                <label>Кількість осіб</label>
                                <input type="text" name="country" placeholder=""></input>
                            </div>
                            
                        </div>
                        <div className="row form-buttons">
                            <button className="btn-danger">Розширений пошук</button>
                            <button className="btn-success">Знайти тури</button>
                        </div>
                        
                    </form>
                </div>
            </Fragment>
        )
    }
}
export default EasyForm