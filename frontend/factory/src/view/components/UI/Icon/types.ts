import React from 'react';
import { ICON } from './IconType';

export interface IIconProps {
    icon: ICON;
    size?: 'sm' | 'md' | 'lg' | 'xs';
    width?: number | string;
    height?: number | string;
    color?: string;
    className?: string;
    style?: React.CSSProperties;
    onClick?: React.MouseEventHandler<HTMLElement>;
    onMouseEnter?: () => void;
    onMouseLeave?: () => void;
}
