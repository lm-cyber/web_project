import React from 'react';
import classNames from 'classnames';
import styles from './index.module.scss';

const cx = classNames.bind(styles);

interface ITitleProps {
    name: string;
}
export const Title: React.FC<ITitleProps> = (props) => {
    return <div className={cx(styles.title)}>{props.name}</div>;
};
