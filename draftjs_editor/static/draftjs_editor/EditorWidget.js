'use strict';

// Global target for exports.
var exports = window.Draft;

// Local identifiers of required modules.
var React = window.React;
var Editor = window.Draft.Editor;
var RichUtils = window.Draft.RichUtils;
var EditorState = window.Draft.EditorState;
var convertFromRaw = window.Draft.convertFromRaw;
var convertToRaw = window.Draft.convertToRaw;
var StyleControls = window.Draft.StyleControls;

var e = React.createElement;

/**
 * React editor component to control value of child input.
 *
 * @param props.blockTypes: *
 * @param props.inlineStyles: *
 * @param props.children: HTMLInputElement | HTMLTextAreaElement
 */
exports.EditorWidget = function EditorWidget(props) {

    props = Object.assign({}, props, useEditorInput(props.children));
    delete props.children;

    var blockType = props.editorState
        .getCurrentContent()
        .getBlockForKey(props.editorState.getSelection().getStartKey())
        .getType();
    var blockTypes = props.blockTypes;
    delete props.blockTypes;

    var inlineStyle = props.editorState.getCurrentInlineStyle();
    var inlineStyles = props.inlineStyles;
    delete props.inlineStyles;

    return (
        e(React.Fragment, null,
            e(StyleControls, {
                isActive: function(type) {
                    return type === blockType;
                },
                onToggle: function(type) {
                    props.onChange(
                        RichUtils.toggleBlockType(
                            props.editorState,
                            type
                        )
                    )
                },
            }, blockTypes),
            e(StyleControls, {
                isActive: function (style) {
                    return inlineStyle.has(style);
                },
                onToggle: function (style) {
                    props.onChange(
                        RichUtils.toggleInlineStyle(
                            props.editorState,
                            style
                        )
                    );
                }
            }, inlineStyles),
            e('div', {
                className: 'RichEditor-editor'
            }, e(Editor, props))
        )
    );
};

/**
 * Use editor state bound to input.value.
 *
 * @param input: HTMLElement
 *
 * @returns *: {onChange: Function, editorState: EditorState}
 */
function useEditorInput(input) {
    var initialContent = React.useRef(null);

    if(initialContent.current === null && input.value) {
        var rawContent = JSON.parse(input.value);
        if(rawContent) {
            try {
                initialContent.current = convertFromRaw(rawContent);
            }
            catch (error) {
                console.error(error);
            }
        }
    }

    var editorState = React.useState(
        initialContent.current
            ? EditorState.createWithContent(initialContent.current)
            : EditorState.createEmpty()
    );
    var setEditorState = editorState[1];
    editorState = editorState[0];

    return {
        editorState: editorState,
        onChange: function(editorState) {
            setEditorState(editorState);
            var rawContent = convertToRaw(editorState.getCurrentContent());
            input.value = JSON.stringify(rawContent);
        }
    };
}
