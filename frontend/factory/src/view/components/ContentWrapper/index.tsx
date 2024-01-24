import React from 'react';
import { ReactNode } from 'react';
import classNames from 'classnames';
import styles from './index.module.scss';

const cx = classNames.bind(styles);

interface IContentWrapper {
    children: ReactNode;
}

export const ContentWrapper: React.FC<IContentWrapper> = (props) => {
    return <div className={cx(styles.contentWrapper)}>{props.children}</div>;
};
