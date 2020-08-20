import React from "react";
import './header.css';
import logoimg from '../../templates/img/LogoIdeaTour.svg';

export default class Header extends React.Component {
    constructor(props){
        super(props)
        this.state={}
    }
    render() {
        return (
        <React.Fragment>
            <div className="header">
                <div className="header-burger">
                <img src={logoimg} className="logo"/>
                    <a href="#" className="burger-button">
                        <span></span>
                    </a>
                </div>
                <ul className="first-ul">
                    <li><a href="#">Усі тури</a></li>
                    <li><a href="#">Гарячі тури</a></li>
                    <li><a href="#">Блог</a></li>
                    <li><a href="#">Інформація</a></li>
                </ul>
                <span className="header-contacts">
                    <p>з 9:00 до 22:00 щодня</p>
                    <p className="phone-number">0 800 500 505</p>
                </span>
                <ul className="second-ul">
                    <li>укр</li>
                    <li><i className="far fa-heart"></i></li>
                    <li><i className="far fa-user"></i></li>
                </ul>
            </div>
        </React.Fragment>
        )
    }
}